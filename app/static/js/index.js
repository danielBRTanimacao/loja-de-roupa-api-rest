async function buscarDados() {
    const url = "http://127.0.0.1:8000/api/roupas/";
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Erro ao buscar os dados");

        const data = await response.json();
        document.getElementById("resultado").innerHTML = "";
        data.forEach((e) => {
            document.getElementById("resultado").innerHTML += `
            <li>          
                <strong>ID:</strong> ${e.id}<br>
                <strong>Nome:</strong> ${e.name}<br>
                <strong>Valor:</strong> R$${e.value}<br>
                <strong>Estoque:</strong> ${e.stock}
            </li>`;
        });
    } catch (error) {
        document.getElementById("resultado").innerHTML =
            "Erro: " + error.message;
    }
}
