# NX-AGENT-7010 — Memory Schema

| Field | Value |
|-------|-------|
| **Document ID** | NX-AGENT-7010 |
| **Title** | Memory Schema |
| **Phase** | 4 — AI Brain |
| **Owner** | AI Platform AI |
| **Status** | 🟢 Complete |
| **Version** | 0.1.0 |
| **Created** | 2026-06-30 |
| **Depends on** | NX-AGENT-7001 (Contract), Memory Engine (NX-FEAT-1700) |

---

## 1. Purpose

This document defines the **schema** for what agents read and write to the Memory Engine. It is the contract between the agent runtime and the memory layer.

## 2. Memory item

The atomic unit of memory:

```typescript
interface MemoryItem {
  id: string;                  // UUID v7
  type: MemoryType;
  scope: MemoryScope;
  key?: string;                // for preference / config
  value: any;                  // typed by type
  source: MemorySource;
  confidence: number;          // 0–1, for inferences
  ttl_ms?: number;             // optional expiry
  pinned: boolean;             // prevent auto-deletion
  created_at: timestamp;
  updated_at: timestamp;
  accessed_count: number;
  last_accessed_at?: timestamp;
  metadata?: Record<string, any>;
}

type MemoryType =
  | 'preference'
  | 'project_fact'
  | 'conversation_summary'
  | 'style_profile'
  | 'entity'
  | 'relation'
  | 'document_chunk'
  | 'agent_decision'
  | 'workflow_state'
  | 'feedback';

interface MemoryScope {
  level: 'user' | 'workspace' | 'global' | 'public';
  workspace_id?: string;
  user_id?: string;
}

interface MemorySource {
  type: 'user_explicit' | 'user_inferred' | 'agent_extracted' | 'system' | 'imported';
  agent_id?: string;
  conversation_id?: string;
  artifact_id?: string;
  url?: string;
  reliability?: 'high' | 'medium' | 'low';
}
```

## 3. Memory types in detail

### 3.1 Preference

User-stated or inferred preferences.

```typescript
interface PreferenceItem extends MemoryItem {
  type: 'preference';
  key: string;                 // 'tone', 'output_length', 'language', 'theme'
  value: string | number | boolean;
}
```

Examples: tone=casual, output_length=standard, language=en.

### 3.2 Project fact

Facts about a Workspace.

```typescript
interface ProjectFactItem extends MemoryItem {
  type: 'project_fact';
  workspace_id: string;
  claim: string;
  evidence?: string;
  source_url?: string;
  confidence: number;
}
```

Examples: "Acme Corp raised list price 12% on Mar 3, 2027."

### 3.3 Conversation summary

Distilled facts from conversations.

```typescript
interface ConversationSummaryItem extends MemoryItem {
  type: 'conversation_summary';
  conversation_id: string;
  participants: string[];
  facts: ProjectFactItem[];
}
```

### 3.4 Style profile

User's writing style.

```typescript
interface StyleProfileItem extends MemoryItem {
  type: 'style_profile';
  profile: {
    tone: 'formal' | 'neutral' | 'casual';
    length: 'brief' | 'standard' | 'detailed';
    format: 'prose' | 'bullets' | 'mixed';
    samples: string[];         // 5+ samples used to derive profile
  };
}
```

### 3.5 Entity

Entities in the knowledge graph.

```typescript
interface EntityItem extends MemoryItem {
  type: 'entity';
  name: string;
  entity_type: 'person' | 'company' | 'product' | 'concept' | 'place' | 'event';
  attributes: Record<string, string | number | boolean>;
  aliases: string[];
}
```

### 3.6 Relation

Edges between entities.

```typescript
interface RelationItem extends MemoryItem {
  type: 'relation';
  from_entity_id: string;
  to_entity_id: string;
  relation_type: string;       // 'works_at', 'owns', 'related_to'
  attributes?: Record<string, any>;
}
```

### 3.7 Document chunk

For RAG over user documents.

```typescript
interface DocumentChunkItem extends MemoryItem {
  type: 'document_chunk';
  document_id: string;
  chunk_index: number;
  text: string;
  embedding: number[];         // vector
  metadata: {
    page?: number;
    section?: string;
    start_char?: number;
    end_char?: number;
  };
}
```

### 3.8 Agent decision

Recorded decisions made by agents.

```typescript
interface AgentDecisionItem extends MemoryItem {
  type: 'agent_decision';
  agent_id: string;
  decision: string;
  reasoning: string;
  alternatives_considered: string[];
  chosen_because: string;
}
```

### 3.9 Workflow state

State for ongoing workflows.

```typescript
interface WorkflowStateItem extends MemoryItem {
  type: 'workflow_state';
  workflow_id: string;
  step: string;
  state: Record<string, any>;
  next_step?: string;
}
```

### 3.10 Feedback

User feedback on agent outputs.

```typescript
interface FeedbackItem extends MemoryItem {
  type: 'feedback';
  target_id: string;           // agent, plan, response
  sentiment: 'positive' | 'neutral' | 'negative';
  comment?: string;
  correction?: string;          // what was wrong + what should be
}
```

## 4. Memory operations

Agents perform these operations:

### 4.1 Read

```typescript
interface ReadRequest {
  scopes: MemoryScope[];
  types?: MemoryType[];
  query?: string;              // semantic
  filters?: Record<string, any>;
  limit?: number;               // default 50
  relevance_threshold?: number; // default 0.7
}

interface ReadResponse {
  items: MemoryItem[];
  relevance_scores: Record<string, number>;
  total_count: number;
}
```

### 4.2 Write

```typescript
interface WriteRequest {
  item: MemoryItem;             // omit id; orchestrator assigns
  if_not_exists?: boolean;
  update_existing?: boolean;
}

interface WriteResponse {
  id: string;
  deduplicated: boolean;        // true if merged with existing
}
```

### 4.3 Update

```typescript
interface UpdateRequest {
  id: string;
  updates: Partial<MemoryItem>;
  reason: string;               // required for audit
}
```

### 4.4 Delete

```typescript
interface DeleteRequest {
  id: string;
  reason: string;               // required for audit
}
```

### 4.5 Search

```typescript
interface SearchRequest {
  query: string;
  scopes: MemoryScope[];
  hybrid?: boolean;             // keyword + semantic
  limit?: number;
}

interface SearchResponse {
  items: MemoryItem[];
  scores: Record<string, number>;
}
```

## 5. Memory scope rules

| Scope | Who reads | Who writes |
|-------|-----------|------------|
| `user` | The user, agents acting for the user | User, agents with `memory.write.user` |
| `workspace` | Workspace members, agents in Workspace | Agents with `memory.write.workspace` |
| `global` | Any of user's agents | User only |
| `public` | Any agent | System |

Cross-scope reads require explicit elevation.

## 6. Privacy and retention

- Memory is encrypted at rest (NX-FEAT-1712).
- Memory is included in account export (NX-FEAT-2009).
- Memory is deleted on account deletion after 30 days (NX-FEAT-2008).
- Default TTL: 90 days for conversation_summary; never for preferences.

## 7. Performance budgets

| Operation | Latency budget |
|-----------|----------------|
| Read (50 items) | <100ms |
| Write | <200ms |
| Update | <200ms |
| Search | <500ms |
| RAG retrieval | <500ms |

## 8. Acceptance criteria

- [ ] All memory types have defined schemas.
- [ ] All operations have defined requests/responses.
- [ ] Scope enforcement verified.
- [ ] Privacy and retention rules enforced.

## 9. Open questions

- Q: Should we support memory "channels" within a Workspace (e.g., research-only)?
- Q: Should we expose memory to plugins?

## 10. Reading list

- **Agent Contract** — NX-AGENT-7001
- **Memory Engine Anchor** — NX-FEAT-1700
- **Memory leaves** — NX-FEAT-1701-1714

---

*End NX-AGENT-7010.*