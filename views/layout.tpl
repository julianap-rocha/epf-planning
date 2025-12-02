<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planning - {{title or 'App'}}</title>
    
    <link rel="stylesheet" href="/static/css/style.css?v=2">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <header class="main-header">
        <a href="/" class="brand">
            <i style="color: var(--primary);"></i> Planning
        </a>

        <nav class="nav-gap">
        <button id="theme-toggle" class="btn-icon" style="font-size: 1.2rem; margin-right: 10px;" title="Mudar Tema">
                <i class="fas fa-moon"></i>
            </button>
            % if defined('usuario') and usuario:
                <div class="user-badge">
                    <i class="fas fa-user-circle"></i> {{usuario.nome.split()[0]}}
                </div>
                <a href="/dashboard" class="nav-link">Dashboard</a>
                <a href="/logout" class="nav-link" style="color: var(--danger);">Sair</a>
            % else:
                <a href="/login" class="nav-link">Entrar</a>
                <a href="/cadastro" class="btn-nav-primary">Criar Conta</a>
            % end
        </nav>
    </header>

    <main class="container">
        {{!base}}
    </main>

    <footer>
        <p>&copy; 2025 Planning - Juliana e Maeli.</p>
    </footer>
    <script src="/static/js/main.js"></script>
</body>
</html>