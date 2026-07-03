# NX-AGENT-7011 — Tool Schema

| Field | Value |
|-------|-------|
| **Document ID** | NX-AGENT-7011 |
| **Title** | Tool Schema |
| **Phase** | 4 — AI Brain |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-AGENT-7001 (Contract) |

---

## 1. Purpose

Tools are **LLM-callable functions** that agents invoke to take action in the world. This document defines the universal tool schema — the contract every tool must satisfy to be agent-callable.

## 2. Why a tool schema

Without it:

- Each tool has its own interface; agents can't reason generically.
- Tools are unauditable; permissions are unclear.
- Composing tools is ad-hoc.

With it:

- Agents can call any tool via a uniform interface.
- Permissions are enforced.
- Composition is composable.

## 3. Tool manifest

Every tool has a manifest:

```typescript
interface Tool {
  id: string;                  // reverse-DNS, e.g., 'browser.search'
  name: string;                // human-readable
  description: string;         // for LLM context; markdown allowed
  category: ToolCategory;
  version: semver;
  owner: string;

  // Inputs
  parameters: ToolParameters;  // JSON Schema

  // Outputs
  returns: ToolReturn;

  // Behavior
  side_effects: SideEffect[];
  idempotent: boolean;
  timeout_ms: number;

  // Cost
  estimated_cost_usd: number;  // typical
  max_cost_usd: number;        // ceiling

  // Permissions
  permissions_required: string[];

  // Safety
  dangerous: boolean;
  requires_approval: boolean;
}

type ToolCategory =
  | 'browser'
  | 'file'
  | 'shell'
  | 'network'
  | 'memory'
  | 'model'
  | 'agent'
  | 'workflow'
  | 'integration'
  | 'system';
```

## 4. Parameters

Tool parameters are declared as **JSON Schema**:

```typescript
interface ToolParameters {
  type: 'object';
  properties: Record<string, JSONSchema>;
  required?: string[];
  additionalProperties?: boolean;
}

interface JSONSchema {
  type: 'string' | 'number' | 'integer' | 'boolean' | 'array' | 'object' | 'null';
  description: string;          // critical for LLM context
  enum?: any[];
  default?: any;
  minimum?: number;
  maximum?: number;
  pattern?: string;
  items?: JSONSchema;          // for arrays
  properties?: Record<string, JSONSchema>; // for objects
}
```

Example:

```typescript
{
  type: 'object',
  properties: {
    url: {
      type: 'string',
      description: 'Absolute URL to fetch. Must include protocol.',
      pattern: '^https?://'
    },
    method: {
      type: 'string',
      enum: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
      default: 'GET'
    },
    headers: {
      type: 'object',
      description: 'HTTP headers as key-value pairs',
      additionalProperties: { type: 'string' }
    },
    body: {
      type: 'string',
      description: 'Request body (for POST/PUT/PATCH). String or JSON-encoded.'
    },
    timeout_ms: {
      type: 'integer',
      minimum: 1000,
      maximum: 60000,
      default: 10000
    }
  },
  required: ['url']
}
```

## 5. Return

```typescript
interface ToolReturn {
  type: 'object';
  properties: Record<string, JSONSchema>;
  required?: string[];
}

interface ToolResult {
  success: boolean;
  output?: any;
  error?: ToolError;
  artifacts?: Artifact[];
  metrics: {
    duration_ms: number;
    cost_usd: number;
    bytes_in?: number;
    bytes_out?: number;
  };
}

interface ToolError {
  code: string;                // 'timeout', 'unauthorized', 'rate_limit', 'invalid_input', 'not_found', 'internal'
  message: string;
  retryable: boolean;
  retry_after_ms?: number;
}
```

## 6. Side effects

```typescript
type SideEffect =
  | 'none'
  | 'reads_data'
  | 'writes_data'
  | 'sends_message'
  | 'creates_account'
  | 'spends_money'
  | 'modifies_state';
```

Tools declare their side effects. The orchestrator uses this for:

- Permission scoping.
- Approval gating.
- User notifications.

## 7. Examples

### 7.1 `browser.search`

```yaml
id: browser.search
name: Web Search
description: Search the web using the configured search engine. Returns top results.
category: browser
version: 1.0.0
parameters:
  type: object
  properties:
    query:
      type: string
      description: Search query
    num_results:
      type: integer
      minimum: 1
      maximum: 50
      default: 10
  required: [query]
returns:
  type: object
  properties:
    results:
      type: array
      items:
        type: object
        properties:
          url: { type: string }
          title: { type: string }
          snippet: { type: string }
side_effects: [reads_data]
idempotent: true
timeout_ms: 10000
estimated_cost_usd: 0.001
permissions_required: [browser.session.use]
dangerous: false
requires_approval: false
```

### 7.2 `email.send`

```yaml
id: email.send
name: Send Email
description: Send an email via the user's connected email account.
category: integration
version: 1.0.0
parameters:
  type: object
  properties:
    to:
      type: string
      description: Recipient email
    subject:
      type: string
    body:
      type: string
    cc:
      type: array
      items: { type: string }
    attachments:
      type: array
      items: { type: string }
  required: [to, subject, body]
returns:
  type: object
  properties:
    message_id: { type: string }
side_effects: [sends_message, writes_data]
idempotent: false
timeout_ms: 30000
estimated_cost_usd: 0.005
permissions_required: [email.send, credential.use]
dangerous: true
requires_approval: true
```

### 7.3 `shell.execute`

```yaml
id: shell.execute
name: Run Shell Command
description: Execute a shell command in the user's local environment or Cloud Browser.
category: shell
version: 1.0.0
parameters:
  type: object
  properties:
    command:
      type: string
    cwd:
      type: string
    timeout_ms:
      type: integer
      default: 30000
  required: [command]
side_effects: [writes_data, modifies_state]
idempotent: false
timeout_ms: 60000
estimated_cost_usd: 0.001
permissions_required: [shell.execute]
dangerous: true
requires_approval: true
```

## 8. The tool registry

The orchestrator maintains a registry of all available tools:

```typescript
interface ToolRegistry {
  tools: Map<string, Tool>;
  by_category: Map<ToolCategory, string[]>;
  by_agent_role: Map<AgentRole, string[]>;
  register(tool: Tool): void;
  unregister(tool_id: string): void;
  get(tool_id: string): Tool;
  list(filters?: ToolFilters): Tool[];
}
```

Tools are registered at:

- NEXUS startup (built-in tools).
- Plugin install (per NX-FEAT-1902).
- Agent load (agent-specific tools).

## 9. Tool invocation

The agent invokes a tool via:

```typescript
interface ToolInvocation {
  tool_id: string;
  arguments: Record<string, any>;
  idempotency_key?: string;
  approval_grant?: ApprovalGrant;
}

interface ApprovalGrant {
  user_id: string;
  granted_at: timestamp;
  expires_at?: timestamp;
  scope: string;
  signature: string;
}
```

The orchestrator:

1. Validates arguments against schema.
2. Checks permissions.
3. Checks approval (if required).
4. Calls tool.
5. Returns result.
6. Logs to audit.

## 10. Composition

Tools compose: an agent can chain tool calls.

```mermaid
graph LR
    A[Plan Step] --> T1[Tool 1]
    T1 --> T2[Tool 2]
    T2 --> T3[Tool 3]
    T3 --> R[Result]
```

Composition is the agent's responsibility, not the orchestrator's.

## 11. Built-in tools (H1)

A non-exhaustive list:

| Tool | Category | Idempotent | Approval |
|------|----------|-----------|----------|
| `browser.search` | browser | ✅ | no |
| `browser.read` | browser | ✅ | no |
| `browser.click` | browser | ✅ | no |
| `browser.type` | browser | ✅ | no |
| `browser.extract` | browser | ✅ | no |
| `file.read` | file | ✅ | no |
| `file.write` | file | ❌ | yes |
| `shell.execute` | shell | ❌ | yes |
| `network.http` | network | configurable | configurable |
| `memory.read` | memory | ✅ | no |
| `memory.write` | memory | ✅ | no |
| `model.summarize` | model | ✅ | no |
| `agent.message` | agent | ❌ | no |
| `workflow.execute` | workflow | ❌ | no |
| `email.send` | integration | ❌ | yes |
| `chat.post` | integration | ❌ | yes |
| `social.post` | integration | ❌ | yes |
| `git.commit` | integration | ❌ | yes |
| `git.push` | integration | ❌ | yes |
| `deploy.trigger` | integration | ❌ | yes |
| `notification.send` | system | ✅ | no |
| `audit.record` | system | ✅ | no |

## 12. Performance

- Tool dispatch latency: <50ms (excluding tool execution).
- Argument validation: <10ms.
- Permission check: <10ms.

## 13. Acceptance criteria

- [ ] Every tool has a manifest.
- [ ] Schemas validate at registration.
- [ ] Side effects declared and enforced.
- [ ] Approval gating works.
- [ ] Tools discoverable by agent role.

## 14. Open questions

- Q: Should we support tool versioning with deprecation windows?
- Q: Should we expose tool search to LLM?
- Q: How do we handle tools that take minutes/hours (e.g., deploy)?

## 15. Reading list

- **Agent Contract** — NX-AGENT-7001
- **Communication Protocol** — NX-AGENT-7009
- **Plugin SDK** — NX-FEAT-1901-1909

---

*End NX-AGENT-7011.*