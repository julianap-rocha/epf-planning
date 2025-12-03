% rebase('layout.tpl', title='Minhas Notas')

<div class="table-header">
    <h2 style="font-weight: 800; color: var(--secondary);">Minhas Notas ⭐</h2>
    <a href="/notas/adicionar" class="btn-nav-primary" style="background: var(--success);"><i class="fas fa-plus"></i>
        Nova Nota</a>
</div>
% if not notas:
<div class="card-box" style="padding: 3rem; text-align: center; color: var(--text-gray);">
    <i class="fas fa-clipboard-check" style="font-size: 3rem; margin-bottom: 1rem; color: #e2e8f0;"></i>
    <p style="font-weight: 600;">Nenhuma nota lançada.</p>
</div>
% else:
<table class="clean-table">
    <thead>
        <tr>
            <th>Matéria</th>
            <th>Avaliação</th>
            <th>Nota</th>
            <th style="text-align: right;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for n in notas:
        <tr>
            <td style="font-weight: 700;">{{n.materia}}</td>
            <td>{{n.nome_prova}}</td>
            <td><span
                    style="background: #f0fff4; color: var(--success); padding: 6px 14px; border-radius: 20px; font-weight: 800; border: 1px solid #b2f5ea;">{{n.valor}}</span>
            </td>
            <td style="text-align: right;">
                <a href="/notas/editar/{{n.id}}" class="btn-icon btn-edit"><i class="fas fa-pen"></i></a>
                <form action="/notas/excluir/{{n.id}}" method="post" style="display:inline;"
                    onsubmit="return confirm('Apagar?');">
                    <button type="submit" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>
% end
<div style="margin-top: 2rem;"><a href="/dashboard"
        style="color: var(--text-gray); text-decoration: none; font-weight: 700;">&larr; Voltar</a></div>