# Guia de GitHub do zero ao Pull Request

Este guia foi feito para quem nunca usou GitHub.

---

## 1. O que é Git?

Git é uma ferramenta que guarda o histórico do seu projeto.

Pense assim:

- você altera arquivos hoje
- amanhã altera de novo
- depois percebe que algo quebrou

Com o Git, você consegue:

- salvar versões do projeto
- voltar para versões antigas
- trabalhar em melhorias sem estragar a versão principal

---

## 2. O que é GitHub?

GitHub é o site onde você publica o seu projeto com Git.

Pense assim:

- **Git** = ferramenta de versionamento
- **GitHub** = plataforma online onde seu projeto fica hospedado

---

## 3. O que é commit?

Commit é como se fosse uma “foto” do projeto em um determinado momento.

Exemplo:

- você terminou a análise inicial
- salva com um commit

Mensagem boa de commit:
```bash
git commit -m "feat: add initial sales analysis"
```

Isso significa:
> “salvei esta etapa do projeto”

---

## 4. O que é branch?

Branch é uma linha separada de trabalho.

A branch principal normalmente se chama `main`.

Você pode criar outra branch, por exemplo `develop`, para fazer mudanças sem mexer diretamente na versão principal.

Pense assim:

- `main` = versão principal
- `develop` = versão onde você desenvolve melhorias

No seu case, a empresa pediu exatamente isso:
- manter a análise principal na `main`
- criar a `develop`
- adicionar nela o top 10 por categoria
- abrir um Pull Request para juntar `develop` com `main`

---

## 5. O que é Pull Request (PR)?

Pull Request é um pedido para juntar uma branch em outra.

No seu caso:

- você cria a branch `develop`
- faz a melhoria nela
- abre um Pull Request para unir `develop` -> `main`

É como dizer:

> “Terminei a melhoria. Quero que ela entre na versão principal.”

---

## 6. Instalação do Git

### Windows
1. Acesse o site oficial do Git
2. Baixe o instalador
3. Instale clicando em “Next” até o final

### Verificar instalação
Abra o terminal e rode:

```bash
git --version
```

Se aparecer uma versão, está instalado.

---

## 7. Criando conta no GitHub

1. Entre no GitHub
2. Clique em **Sign up**
3. Crie sua conta
4. Confirme o e-mail

---

## 8. Configuração inicial do Git no seu computador

No terminal, rode:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

Isso grava seu nome e e-mail para os commits.

Você pode conferir com:

```bash
git config --global --list
```

---

## 9. Criando o projeto localmente

1. Crie uma pasta chamada `case_analytics_vendas`
2. Coloque todos os arquivos do projeto dentro dela
3. Abra o terminal nessa pasta

---

## 10. Iniciando o Git no projeto

Dentro da pasta do projeto, rode:

```bash
git init
```

Isso transforma a pasta em um repositório Git.

---

## 11. Adicionando arquivos para controle de versão

```bash
git add .
```

Esse comando prepara todos os arquivos para o commit.

---

## 12. Criando o primeiro commit

```bash
git commit -m "feat: initial sales analysis project"
```

Esse é o primeiro registro oficial do projeto.

---

## 13. Criando o repositório no GitHub

No GitHub:

1. clique em **New repository**
2. dê o nome `case-analytics-vendas`
3. deixe como público, se não houver restrição
4. clique em **Create repository**

Depois o GitHub vai te mostrar comandos.

---

## 14. Ligando seu projeto local ao GitHub

No terminal, rode algo parecido com isto:

```bash
git remote add origin https://github.com/SEU_USUARIO/case-analytics-vendas.git
```

Agora seu projeto local está conectado ao GitHub.

---

## 15. Enviando a branch main para o GitHub

Primeiro garanta que sua branch principal se chama `main`:

```bash
git branch -M main
```

Depois envie:

```bash
git push -u origin main
```

Pronto: seu projeto já está publicado.

---

## 16. Criando a branch develop

Agora você vai criar a branch pedida no case:

```bash
git checkout -b develop
```

Esse comando faz duas coisas:
- cria a branch `develop`
- já te coloca dentro dela

Você pode conferir com:

```bash
git branch
```

A branch atual aparece com um `*`.

---

## 17. Fazendo a melhoria pedida na develop

Na branch `develop`, você pode:

- adicionar a função de top 10 por categoria
- atualizar o README
- gerar novos outputs

Depois disso:

```bash
git add .
git commit -m "feat: add top 10 products by category"
git push -u origin develop
```

---

## 18. Abrindo o Pull Request

No GitHub:

1. entre no repositório
2. normalmente vai aparecer um botão como **Compare & pull request**
3. clique nele
4. confirme que está assim:

- base: `main`
- compare: `develop`

5. no título do PR, escreva algo como:

`feat: add top 10 products by category`

6. na descrição, explique o que foi feito

Exemplo:

```text
This PR adds the top 10 products by category analysis requested in the case.

Changes:
- created category mapping
- added top 10 ranking within each category
- updated README with new explanation
```

7. clique em **Create pull request**

Pronto. Você cumpriu exatamente o que o case pediu.

---

## 19. Ordem completa do que você vai fazer

### Etapa 1 - Projeto inicial
```bash
git init
git add .
git commit -m "feat: initial sales analysis project"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/case-analytics-vendas.git
git push -u origin main
```

### Etapa 2 - Branch develop
```bash
git checkout -b develop
git add .
git commit -m "feat: add top 10 products by category"
git push -u origin develop
```

### Etapa 3 - Pull Request
Faça pelo site do GitHub, juntando:
- `develop` -> `main`

---

## 20. Commits sugeridos

Se quiser deixar mais organizado, você pode fazer vários commits menores:

```bash
git commit -m "chore: create project structure"
git commit -m "feat: add descriptive analysis"
git commit -m "feat: add monthly revenue chart"
git commit -m "docs: add execution instructions to README"
git commit -m "feat: add top 10 products by category"
```

---

## 21. Erros comuns de iniciantes

### Erro 1: esquecer de rodar `git add .`
Sem isso, o commit não pega suas alterações.

### Erro 2: alterar na branch errada
Antes de mexer, confira:
```bash
git branch
```

### Erro 3: não dar push
O commit salva localmente.  
O `git push` envia para o GitHub.

### Erro 4: abrir PR invertido
No case, o correto é:
- **base = main**
- **compare = develop**

---

## 22. O que falar na entrega

Você pode dizer algo como:

> Desenvolvi a análise descritiva em Python com foco em produtos mais vendidos, faturamento mensal e ticket médio por cliente. Organizei o projeto com estrutura de pastas, README, outputs e versionamento com Git/GitHub. Também criei a branch `develop` com a análise adicional de top 10 por categoria e abri o Pull Request conforme solicitado no case.

---

## 23. Checklist final antes de entregar

- [ ] projeto sobe e roda sem erro
- [ ] README explica como executar
- [ ] requirements.txt existe
- [ ] branch `main` criada
- [ ] branch `develop` criada
- [ ] melhoria pedida está na `develop`
- [ ] PR aberto de `develop` para `main`
- [ ] commits com mensagens claras