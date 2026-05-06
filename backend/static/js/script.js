document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-pergunta');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const resposta = document.querySelector('input[name="resposta"]:checked');
            
            if (!resposta) {
                e.preventDefault();
                alert('Por favor, selecione uma alternativa!');
            }
        });
    }
    
    const alternativas = document.querySelectorAll('.alternativa');
    alternativas.forEach(alt => {
        alt.addEventListener('click', function() {
            const radio = this.querySelector('input[type="radio"]');
            if (radio) {
                radio.checked = true;
            }
        });
    });
});
