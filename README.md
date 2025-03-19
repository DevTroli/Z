# <div align="center">🚀 Projeto Z - A Plataforma de Mídia Social do Futuro</div>

<div align="center">
  <strong>Uma rede social inovadora inspirada no X (antigo Twitter), com Zweets, interações em tempo real e uma experiência de usuário incomparável!</strong>
</div>

<div align="center">
  <a href="#visão-geral">Visão Geral</a> •
  <a href="#funcionalidades-principais">Funcionalidades</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#sprints">Sprints</a> •
  <a href="#segurança">Segurança</a> •
  <a href="#contribuição">Contribuição</a> •
  <a href="#licença">Licença</a>
</div>

<br>

## 📌 Visão Geral <a name="visão-geral"></a>

O **Projeto Z** é uma plataforma de mídia social simples & moderna , projetada para oferecer uma experiência de usuário fluida e interativa.
Desenvolvido com uma stack tecnológico robusta, o projeto implementa as melhores práticas de desenvolvimento, garantindo código limpo, testável e manutenível.

### 💡 Por que escolher o Z?

- **Interações em tempo real** - Receba notificações instantâneas e veja atualizações sem recarregar
- **Interface intuitiva** - Design moderno e responsivo utilizando Tailwind CSS
- **Segurança avançada** - Implementação robusta de autenticação e proteção de dados

<br>

## ✨ Funcionalidades Principais <a name="funcionalidades-principais"></a>

### 🌟 Experiência do Usuário
- **Zweets** - Compartilhe pensamentos e ideias em até 280 caracteres
- **Feed personalizado** - Conteúdo adaptado às suas preferências e conexões
- **Notificações em tempo real** - Mantenha-se atualizado instantaneamente

### 🤝 Interação Social
- **Sistema de seguidores** - Conecte-se com pessoas que compartilham seus interesses
- **Comentários aninhados** - Participe de conversas estruturadas
- **Likes com atualização em tempo real** - Feedback instantâneo para suas interações

### 👤 Perfil e Identidade
- **Avatares dinâmicos** - Identidade visual personalizada
- **Bio customizável** - Expresse-se para seus seguidores
- **Métricas de engajamento** - Acompanhe o impacto de seu conteúdo

<br>

## 🛠️ Tecnologias <a name="tecnologias"></a>

O Projeto Z utiliza um stack tecnológico moderno e poderoso:

### Backend
- **[Django](https://www.djangoproject.com/)** - Framework web robusto para desenvolvimento rápido
- **[Django REST Framework](https://www.django-rest-framework.org/)** - Toolkit poderoso para construção de APIs
- **[Django Channels](https://channels.readthedocs.io/)** - Suporte para WebSockets e comunicação assíncrona

### Frontend
- **[Tailwind CSS](https://tailwindcss.com/)** - Framework CSS utilitário para design responsivo
- **[Alpine.js](https://alpinejs.dev/)** - Framework JavaScript leve para interatividade
- **[HTMX](https://htmx.org/)** - Acesso a recursos modernos do navegador diretamente do HTML

### Persistência e Comunicação
- **[PostgreSQL](https://www.postgresql.org/)** - Sistema gerenciador de banco de dados relacional
- **[Redis](https://redis.io/)** - Armazenamento de estrutura de dados em memória para cache e mensageria

### Infraestrutura e DevOps
- **[Docker](https://www.docker.com/)** - Containerização para ambientes consistentes
- **[Docker Compose](https://docs.docker.com/compose/)** - Orquestração de múltiplos containers
- **[GitHub Actions](https://github.com/features/actions)** - Automação de CI/CD
- **[PythonAnywhere](https://www.pythonanywhere.com/)** - Plataforma de hospedagem Python

<br>

## 🚀 Instalação <a name="instalação"></a>

### Pré-requisitos
- Docker e Docker Compose instalados em sua máquina
- Python 3.10 ou superior
- Git

### Configuração do Ambiente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/devTroli/Z.git
   cd Z
   ```

2. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   ```
   > ⚠️ **Importante**: Edite o arquivo `.env` com suas configurações específicas

3. **Inicie os containers com Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Acesse a aplicação**
   > 🌐 Navegue para [http://localhost:8000](http://localhost:8000) em seu navegador
   
### Verificação da Instalação
Após a inicialização, você verá o log de inicialização no terminal. Verifique se todos os serviços estão funcionando corretamente.

<br>

## 📂 Estrutura de Diretórios

```
Z/
├── core/                          # Configurações principais do projeto Django
│   ├── __init__.py
│   ├── asgi.py                    # Configuração ASGI para WebSockets
│   ├── settings.py                # Configurações do Django
│   ├── urls.py                    # URLs globais
│   └── wsgi.py                    # Configuração WSGI
│
├── static/                        # Arquivos estáticos
│   └── js/
│       └── feed.js                # JavaScript para o feed de Zweets
│
├── staticfiles/                   # Arquivos estáticos coletados
│   ├── admin/                     # Arquivos do admin do Django
│   ├── django_extensions/         # Arquivos do django-extensions
│   └── js/
│       └── feed.js
│
├── templates/                     # Templates HTML
│   ├── auth/
│   │   ├── login.html             # Página de login
│   │   └── signup.html            # Página de cadastro
│   ├── includes/
│   │   └── navbar.html            # Componente de navegação
│   ├── users/
│   │   ├── edit_profile.html      # Edição de perfil
│   │   └── profile.html           # Perfil de usuário
│   ├── zweets/
│   │   ├── comments.html          # Template de comentários
│   │   ├── feed.html              # Feed principal
│   │   ├── zweet_detail.html      # Detalhe de Zweet
│   │   └── zweet_list.html        # Lista de Zweets
│   └── base.html                  # Template base
│
├── users/                         # Aplicativo de usuários
│   ├── migrations/                # Migrações do banco de dados
│   │   ├── 0001_initial.py        # Migração inicial
│   │   └── 0002_follow.py         # Modelo de seguidores
│   ├── __init__.py
│   ├── admin.py                   # Configuração do admin
│   ├── apps.py                    # Configuração do app
│   ├── forms.py                   # Formulários de usuário
│   ├── models.py                  # Modelos de dados (User, Follow)
│   ├── test.py                    # Testes
│   └── views.py                   # Views do app
│
├── zweets/                        # Aplicativo de Zweets
│   ├── api/                       # API REST
│   │   ├── serializers.py         # Serializadores
│   │   ├── urls.py                # URLs da API
│   │   └── views.py               # Views da API
│   ├── migrations/                # Migrações do banco de dados
│   │   ├── 0001_initial.py        # Migração inicial
│   │   └── 0002_comment.py        # Modelo de comentários
│   ├── __init__.py
│   ├── admin.py                   # Configuração do admin
│   ├── apps.py                    # Configuração do app
│   ├── models.py                  # Modelos de dados (Zweet, Comment)
│   ├── tests.py                   # Testes
│   ├── urls.py                    # URLs das páginas
│   └── views.py                   # Views das páginas
│
├── Dockerfile                     # Configuração Docker
├── docker-compose.yml             # Orquestração de containers
├── manage.py                      # Script de gerenciamento Django
└── requirements.txt               # Dependências do projeto
```

## 🔒 Segurança <a name="segurança"></a>

A segurança é uma prioridade no Projeto Z:

- **HTTPS Obrigatório**
  - Configurado via `SECURE_SSL_REDIRECT`
  - Certificados SSL via Let's Encrypt

- **Headers de Segurança**
  - Proteção contra XSS via Content Security Policy
  - Proteção contra clickjacking via X-Frame-Options
  - Implementação completa de `django-secure`

- **Proteção de Dados**
  - Variáveis sensíveis armazenadas em `.env`
  - Segredos gerenciados via GitHub Secrets
  - Sanitização de inputs para prevenir injeções SQL

- **Autenticação Robusta**
  - Proteção contra força bruta
  - Tokens de sessão seguros
  - Validação de força de senha

<br>

## 🤝 Contribuição <a name="contribuição"></a>

Contribuições são essenciais para o crescimento do Projeto Z! Siga estas diretrizes para contribuir:

### Processo de Contribuição

1. **Verifique as issues existentes**
   > Procure por issues abertas que precisam de ajuda ou crie uma nova para discutir sua ideia.

2. **Faça um fork do repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/Z.git
   cd Z
   git remote add upstream https://github.com/devTroli/Z.git
   ```

3. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```

4. **Desenvolva sua contribuição**
   > Siga o estilo de código do projeto e adicione testes para suas mudanças.

5. **Envie um pull request**
   > Forneça uma descrição detalhada das mudanças e referencie qualquer issue relacionada.

### Diretrizes de Código

- Siga o padrão PEP 8 para código Python
- Adicione testes para novas funcionalidades
- Documente seu código utilizando docstrings
- Mantenha o README atualizado quando necessário

<br>

## 📄 Licença <a name="licença"></a>

Este projeto está licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para mais detalhes.

<br>

## 👨‍💻 Autores e Contribuidores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/devTroli">
        <img src="https://ui-avatars.com/api/?name=Troli" width="100px;" alt="Avatar de Troli"/><br>
        <sub><b>Troli</b></sub>
      </a>
    </td>
    <!-- Adicione mais contribuidores aqui -->
  </tr>
</table>

<br>

---

<div align="center">
  <sub>Feito com ❤️ por <a href="https://github.com/devTroli">DevTroli</a></sub>
</div>
