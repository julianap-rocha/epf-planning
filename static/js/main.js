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

    const eyes = document.querySelectorAll('.toggle-password');

    eyes.forEach(eye => {
        eye.addEventListener('click', function () {

            const wrapper = this.closest('.password-wrapper');
            const input = wrapper.querySelector('.form-input');

            if (input.type === "password") {
                input.type = "text";
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                input.type = "password";
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    });
});

const themeBtn = document.getElementById('theme-toggle');
const themeIcon = themeBtn ? themeBtn.querySelector('i') : null;

if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    if (themeIcon) {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    }
}

if (themeBtn) {
    themeBtn.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');

        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            if (themeIcon) {
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            }
        } else {
            localStorage.setItem('theme', 'light');
            if (themeIcon) {
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            }
        }
    });
}
