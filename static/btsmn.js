
const qtdM = document.getElementById('qtdM');
const qtdMN = document.getElementById('qtdMN');

  function decrement() {
    var quantidade = document.getElementById("quantidade");
    if(parseInt(quantidade.value) > 0){
        quantidade.value = parseInt(quantidade.value) - 1;
        const currentValue = parseInt(qtdMN.textContent);
        qtdMN.textContent = currentValue - 1;
    }else{
        alert("GAVETA VAZIA.!")
    }
  }

  
  function increment() {
    var quantidade = document.getElementById("quantidade");
    quantidade.value = parseInt(quantidade.value) + 1;
    const currentValue = parseInt(qtdM.textContent);
    qtdM.textContent = currentValue + 1;
  }
  
  function decrement_p() {
    var quantidadep = document.getElementById("quantidade_p");
    if(parseInt(quantidadep.value) >= 1){
        quantidadep.value = parseInt(quantidadep.value) - 1;
        const currentValue = parseInt(qtdMNP.textContent);
        qtdMNP.textContent = currentValue - 1;
    }else{
      alert("Registro excluido!")
    }
  }

  function increment_p() {
    var quantidadep = document.getElementById("quantidade_p");
      quantidadep.value = parseInt(quantidadep.value) + 1;
      const currentValue = parseInt(qtdMP.textContent);
      qtdMP.textContent = currentValue + 1;
   
  }