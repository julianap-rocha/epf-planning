% rebase('layout.tpl', title='Criar Conta')

<div class="card-box form-center">
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="margin-bottom: 0.5rem; font-weight: 800;">Crie sua conta 🚀</h2>
    </div>
    <form action="/cadastro" method="post">
        <label class="form-label">NOME COMPLETO</label>
        <input type="text" name="nome" class="form-input" required placeholder="Ex: Ana Silva">

        <label class="form-label">E-MAIL</label>
        <input type="email" name="email" class="form-input" required placeholder="seu@email.com">

        <label class="form-label">CRIE UMA SENHA</label>
        <div class="password-wrapper">
            <input type="password" name="senha" id="senhaCadastro" class="form-input" required
                placeholder="Uma senha segura">
            <i class="fas fa-eye toggle-password" onclick="togglePassword('senhaCadastro', this)"></i>
        </div>


        <button type="submit" class="btn-block" style="background: var(--secondary);">Cadastrar Agora</button>
    </form>
    <div style="text-align: center; margin-top: 1.5rem;">
        <a href="/login" style="color: var(--text-gray); text-decoration: none; font-weight: 600;">Já tem conta? Fazer
            Login</a>
    </div>
</div>