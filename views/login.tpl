% rebase('layout.tpl', title='Login')

<style>
    body {
        height: 100vh;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .container {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 1rem;
    }

    .form-center {
        margin: 0;
        width: 100%;
    }

    @media (max-height: 700px) {
        body { overflow: auto; }
        .container { padding: 40px 1rem; align-items: flex-start; }
    }
</style>

<div class="card-box form-center">
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="margin-bottom: 0.5rem; font-weight: 800;">Bem-vindo de volta 👋</h2>
        <p style="color: var(--text-gray);">Acesse sua conta para continuar.</p>
    </div>

    % if defined('erro') and erro:
        <div style="background: #fff5f5; color: var(--danger); padding: 1rem; border-radius: 16px; margin-bottom: 1.5rem; text-align: center; font-weight: 700;">
            <i class="fas fa-exclamation-circle"></i> {{erro}}
        </div>
    % end

    <form action="/login" method="post">
        <label class="form-label">SEU E-MAIL</label>
        <input type="email" name="email" class="form-input" required placeholder="aluno@email.com">

        <label class="form-label">SUA SENHA</label>
        <input type="password" name="senha" class="form-input" required placeholder="••••••••">

        <button type="submit" class="btn-block">Entrar no Sistema</button>
    </form>
    
    <div style="text-align: center; margin-top: 1.5rem;">
        <a href="/cadastro" style="color: var(--primary); text-decoration: none; font-weight: 700;">Não tem conta? Cadastre-se</a>
    </div>
</div>