% rebase('layout.tpl', title='Professor')

<div class="card-box form-center">
    <h2 style="margin-bottom: 1.5rem; text-align: center; font-weight: 800;">{{'Editar' if professor else 'Novo'}} Professor 📝</h2>
    <form action="{{action}}" method="post">
        <label class="form-label">NOME</label>
        <input type="text" name="nome" class="form-input" required value="{{professor.nome if professor else ''}}">
        <label class="form-label">MATÉRIA</label>
        <input type="text" name="materia" class="form-input" required value="{{professor.materia if professor else ''}}">
        <label class="form-label">EMAIL</label>
        <input type="email" name="email" class="form-input" value="{{professor.email if professor else ''}}">
        <label class="form-label">CONTATO (OU SALA)</label>
        <input type="text" name="contato" class="form-input" required value="{{professor.contato if professor else ''}}">
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <a href="/professores" class="btn-block" style="background: #e2e8f0; color: var(--text-gray); text-decoration: none; box-shadow: none;">Cancelar</a>
            <button type="submit" class="btn-block">Salvar</button>
        </div>
    </form>
</div>