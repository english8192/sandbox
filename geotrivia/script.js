let jsonData = [];
let questions = [];
let questionArr = 

async function loadData() {
    try {
        fetch('outputlist2.json')
        .then(response => response.json())
        .then(data => {
            const questionsArray = data;
            
            // Now you can use the questionsArray freely
            console.log(questionsArray);
        
            // Example: Accessing the first question
            console.log(questionsArray[0].question);
        })

    } catch (error) {
        console.error('Error loading data:', error);
    }
}

function getRandomQuestion() {
    if (questions.length === 0) {
        console.log('No more questions available.');
        return null;
    }
    const randomIndex = Math.floor(Math.random() * questions.length);
    return questions.splice(randomIndex, 1)[0]; // Remove and return a random question
}

function displayQuestion() {
    const currentQuestion = getRandomQuestion();
    if (!currentQuestion) return; // Stop if there are no more questions
    document.getElementById("question").textContent = `${currentQuestion}`;
}

async function init() {
    await loadData();
    console.log(typeof questionArr)
    displayQuestion()
}

init(); // Load data and display the first question
