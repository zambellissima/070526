# Diagramas de Sequência

# Caso de Uso: Criar Sessão

View
↓
Controller
↓
Service
↓
Repository
↓
SQLite

Fluxo:
1. Usuário solicita criação da sessão
2. Controller recebe os dados
3. Service valida regras de negócio
4. Repository salva no banco
5. SQLite persiste os dados
6. Sistema retorna confirmação

---

# Caso de Uso: Registrar Público

View
↓
Controller
↓
Service
↓
Repository
↓
SQLite

Fluxo:
1. Usuário informa público
2. Controller recebe os dados
3. Service valida capacidade
4. Repository atualiza sessão
5. SQLite salva alterações
6. Sistema retorna confirmação
