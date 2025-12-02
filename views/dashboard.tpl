% rebase('layout.tpl', title='Painel')

<h1 style="margin-bottom: 1.5rem; font-weight: 800; color: var(--secondary);">Painel de Controle</h1>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
    <a href="/professores" style="text-decoration: none; color: inherit;">
        <div class="card-box" style="height: 100%; display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div style="background: #fff0f6; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <i class="fas fa-chalkboard-teacher" style="font-size: 2rem; color: var(--primary);"></i>
            </div>
            <h3 style="font-weight: 800;">Professores</h3>
            <p style="color: var(--text-gray); font-size: 0.95rem; margin-top: 0.5rem;">Gerenciar contatos.</p>
        </div>
    </a>
    <a href="/notas" style="text-decoration: none; color: inherit;">
        <div class="card-box" style="height: 100%; display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div style="background: #f0fff4; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <i class="fas fa-star" style="font-size: 2rem; color: var(--success);"></i>
            </div>
            <h3 style="font-weight: 800;">Minhas Notas</h3>
            <p style="color: var(--text-gray); font-size: 0.95rem; margin-top: 0.5rem;">Acompanhe o desempenho.</p>
        </div>
    </a>
    <a href="/faltas" style="text-decoration: none; color: inherit;">
        <div class="card-box" style="height: 100%; display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div style="background: #fff5f5; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <i class="fas fa-clock" style="font-size: 2rem; color: var(--danger);"></i>
            </div>
            <h3 style="font-weight: 800;">Faltas</h3>
            <p style="color: var(--text-gray); font-size: 0.95rem; margin-top: 0.5rem;">Controle de presença.</p>
        </div>
    </a>
</div>