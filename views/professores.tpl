% rebase('layout.tpl', title='Professores')

<div class="table-header">
    <h2 style="font-weight: 800;">Meus Professores 👨‍🏫</h2>
    <a href="/professores/adicionar" class="btn-nav-primary"><i class="fas fa-plus"></i> Novo</a>
</div>
% if not professores:
<div class="card-box" style="padding: 3rem; text-align: center; color: var(--text-gray);">
    <i class="fas fa-folder-open" style="font-size: 3rem; margin-bottom: 1rem; color: #e2e8f0;"></i>
    <p style="font-weight: 600;">Nenhum professor cadastrado.</p>
</div>
% else:
<table class="clean-table">
    <thead>
        <tr>
            <th>Nome</th>
            <th>Matéria</th>
            <th>Email</th>
            <th>Contato ou Sala</th>
            <th style="text-align: right;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for p in professores:
        <tr>
            <td style="font-weight: 700; color: var(--secondary);">{{p.nome}}</td>
            <td><span
                    style="background: #fff0f6; color: var(--primary); padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">{{p.materia}}</span>
            </td>
            <td>{{p.email}}</td>
            <td>{{p.contato}}</td>
            <td style="text-align: right;">
                <a href="/professores/editar/{{p.id}}" class="btn-icon btn-edit"><i class="fas fa-pen"></i></a>
                <form action="/professores/excluir/{{p.id}}" method="post" style="display:inline;"
                    onsubmit="return confirm('Excluir?');">
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