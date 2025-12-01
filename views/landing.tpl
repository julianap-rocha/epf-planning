% rebase('layout.tpl', title='Bem-vindo')

<style>
    body { height: 100vh; overflow: hidden; display: flex; flex-direction: column; }
    .container { flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 0; margin: 0 auto; }
    @media (max-height: 600px) { body { overflow: auto; } .container { padding: 40px 0; } }
</style>

<div style="text-align: center; width: 100%; max-width: 800px;">
    <h1 style="font-size: 3.5rem; font-weight: 800; color: var(--secondary); margin-bottom: 0.5rem; letter-spacing: -1px; line-height: 1.1;">
        Organização Acadêmica 📚
    </h1>
    <p style="color: var(--text-gray); font-size: 1.25rem; max-width: 600px; margin: 1.5rem auto 3rem auto; font-weight: 600;">
        Organize suas pendências de forma simples, <br> administre seu semestre!
    </p>
    <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="/cadastro" class="btn-nav-primary" style="padding: 1rem 3rem; font-size: 1.1rem; border-radius: 50px;">Começar Agora</a>
        <a href="/login" class="nav-link" style="padding: 1rem 3rem; border: 2px solid var(--border); border-radius: 50px; background: white; color: var(--secondary);">Já tenho conta</a>
    </div>
</div>