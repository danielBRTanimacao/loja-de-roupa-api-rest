async function buscarDados() {
    const url = "https://jsonplaceholder.typicode.com/todos/1"; // API pública de exemplo
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Erro ao buscar os dados");

        const data = await response.json();
        document.getElementById("resultado").innerHTML = `
<strong>ID:</strong> ${data.id}<br>
<strong>Título:</strong> ${data.title}<br>
<strong>Completo:</strong> ${data.completed ? "Sim" : "Não"}
`;
    } catch (error) {
        document.getElementById("resultado").innerHTML =
            "Erro: " + error.message;
    }
}
