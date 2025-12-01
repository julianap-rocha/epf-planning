/**
 * Efeitos Visuais para o Sistema Bottle
 * 
 * Inclui:
 * - Animação de carregamento suave
 * - Efeito de hover em botões/tabelas
 * - Feedback visual para formulários
 * - Botão de scroll para topo
 */

document.addEventListener("DOMContentLoaded", function () {
    console.log("Planning System Ready 🚀");
    document.body.style.opacity = 0;
    setTimeout(() => {
        document.body.style.transition = "opacity 0.4s ease";
        document.body.style.opacity = 1;
    }, 50);
});
