% rebase('layout.tpl', title='Nota')

<div class="card-box form-center">
    <h2 style="margin-bottom: 1.5rem; text-align: center; font-weight: 800;">{{'Editar' if nota else 'Nova'}} Nota ⭐
    </h2>
    <form action="{{action}}" method="post">
        <label class="form-label">MATÉRIA</label>
        <input type="text" name="materia" class="form-input" required value="{{nota.materia if nota else ''}}">
        <label class="form-label">AVALIAÇÃO</label>
        <input type="text" name="nome_prova" class="form-input" required value="{{nota.nome_prova if nota else ''}}">
        <label class="form-label">NOTA (0 a 10)</label>
        <input type="number" step="0.1" min="0" max="10" name="valor" class="form-input" required
            value="{{nota.valor if nota else ''}}">
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <a href="/notas" class="btn-block"
                style="background: #e2e8f0; color: var(--text-gray); text-decoration: none; box-shadow: none;">Cancelar</a>
            <button type="submit" class="btn-block" style="background: var(--success);">Salvar</button>
        </div>
    </form>
</div>