% rebase('layout.tpl', title='Minhas Faltas')

<div class="table-header">
    <h2 style="font-weight: 800; color: var(--secondary);">Controle de Faltas 📅</h2>
    <a href="/faltas/adicionar" class="btn-nav-primary" style="background: var(--danger);"><i class="fas fa-plus"></i> Registrar Falta</a>
</div>
% if resumo:
<div style="margin-bottom: 2rem;">
    <h3 style="font-size: 1rem; color: var(--text-gray); margin-bottom: 1rem; font-weight: 700;">RESUMO POR MATÉRIA</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
        % for materia, qtd in resumo.items():
            % cor_fundo = '#fff5f5' if qtd >= 10 else '#f0fff4'
            % cor_texto = 'var(--danger)' if qtd >= 10 else 'var(--success)'
            <div class="card-box" style="padding: 1.5rem; display: flex; align-items: center; justify-content: space-between; background: {{cor_fundo}}; border: 1px solid {{cor_texto}};">
                <div><h4 style="color: var(--secondary); font-weight: 800;">{{materia}}</h4><span style="font-size: 0.85rem; color: var(--text-gray);">Total</span></div>
                <div style="text-align: right;"><span style="font-size: 1.8rem; font-weight: 800; color: {{cor_texto}};">{{qtd}}</span></div>
            </div>
        % end
    </div>
</div>
% end
% if not faltas:
    <div class="card-box" style="padding: 3rem; text-align: center; color: var(--text-gray);">
        <i class="fas fa-smile-beam" style="font-size: 3rem; margin-bottom: 1rem; color: #e2e8f0;"></i>
        <p style="font-weight: 600;">Nenhuma falta registrada.</p>
    </div>
% else:
    <h3 style="font-size: 1rem; color: var(--text-gray); margin-bottom: 1rem; font-weight: 700;">HISTÓRICO</h3>
    <table class="clean-table">
        <thead><tr><th>Matéria</th><th>Data</th><th>Qtd.</th><th style="text-align: right;">Ações</th></tr></thead>
        <tbody>
            % for f in faltas:
            <tr>
                <td style="font-weight: 700;">{{f.materia}}</td>
                <td>{{f.data.split('-')[2]}}/{{f.data.split('-')[1]}}/{{f.data.split('-')[0]}}</td>
                <td><span style="background: #fff5f5; color: var(--danger); padding: 4px 10px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">{{f.quantidade}}</span></td>
                <td style="text-align: right;">
                    <a href="/faltas/editar/{{f.id}}" class="btn-icon btn-edit"><i class="fas fa-pen"></i></a>
                    <form action="/faltas/excluir/{{f.id}}" method="post" style="display:inline;" onsubmit="return confirm('Remover?');">
                        <button type="submit" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button>
                    </form>
                </td>
            </tr>
            % end
        </tbody>
    </table>
% end
<div style="margin-top: 2rem;"><a href="/dashboard" style="color: var(--text-gray); text-decoration: none; font-weight: 700;">&larr; Voltar</a></div>