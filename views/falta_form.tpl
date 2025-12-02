% rebase('layout.tpl', title='Falta')

<div class="card-box form-center">
    <h2 style="margin-bottom: 1.5rem; text-align: center; font-weight: 800;">{{'Editar' if falta else 'Registrar'}} Falta 📅</h2>
    <form action="{{action}}" method="post">
        <label class="form-label">MATÉRIA</label>
        <input type="text" name="materia" class="form-input" required value="{{falta.materia if falta else ''}}">
        <label class="form-label">DATA</label>
        <input type="date" name="data" class="form-input" required value="{{falta.data if falta else ''}}">
        <label class="form-label">QUANTIDADE</label>
        <input type="number" min="1" name="quantidade" class="form-input" required value="{{falta.quantidade if falta else ''}}">
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <a href="/faltas" class="btn-block" style="background: #e2e8f0; color: var(--text-gray); text-decoration: none; box-shadow: none;">Cancelar</a>
            <button type="submit" class="btn-block" style="background: var(--danger);">Salvar</button>
        </div>
    </form>
</div>