# Diagrama de Classes do Domínio

## Classe Cinema

### Atributos
- id
- nome
- cidade
- estado
- endereco
- capacidade

---

## Classe Filme

### Atributos
- id
- titulo
- genero
- classificacao
- duracao
- diretor

---

## Classe Sessao

### Atributos
- id
- data
- horario
- publico

---

# Relacionamentos

## Cinema 1:N Sessao
Um cinema pode possuir várias sessões.

## Filme 1:N Sessao
Um filme pode possuir várias sessões.
