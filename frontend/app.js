// backend/app.js
const openai = require('openai');

const openaiKey = 'YOUR_OPENAI_API_KEY'; // Reemplaza con tu clave de API.

async function predict() {
    const prompt = request.query.prompt;
    try {
        const response = await openai.Completion.create({
            engine: "text-davinci-003",
            prompt: prompt,
            max_tokens: 150,
        });
        return response.choices[0].text;
    } catch (error) {
        console.error("Error en la predicción:", error);
        return "No se pudo generar una respuesta.";
    }
}

app.get('/predict', async (req, res) => {
    const prompt = req.query.prompt;
    if (!prompt) {
        res.status(400).send('Por favor, ingresa un prompt.');
        return;
    }
    const prediction = await predict();
    res.json({ result: prediction });
});
