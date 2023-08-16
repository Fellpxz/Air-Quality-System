// --------------------- Habilitar Edição -------------------------------

const enableEditButtons = document.querySelectorAll(".h-edit-button");

enableEditButtons.forEach(button => {
  button.addEventListener("click", function(event) {
    event.preventDefault(); // Impede o envio do formulário
    const inputFields = this.closest(".view-form").querySelectorAll(".view-input");
    inputFields.forEach(input => {
      input.removeAttribute("readonly");
    });
  });
});