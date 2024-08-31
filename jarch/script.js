document.addEventListener('DOMContentLoaded', () => {
    let questions = [];
    let currentIndex = 0;

    const questionDiv = document.getElementById('question');
    const answerDiv = document.getElementById('answer');
    const showAnswerButton = document.getElementById('showAnswer');
    const nextQuestionButton = document.getElementById('nextQuestion');
    const fileInput = document.getElementById('fileInput');
    const loadFileButton = document.getElementById('loadFile');
    const categoryDollarsDiv = document.getElementById('category-dollars');

    function displayQuestion(index) {
        if (index >= 0 && index < questions.length) {
            const { question, answer, category, dollar_value } = questions[index];
            questionDiv.textContent = question;
            answerDiv.textContent = answer;
            answerDiv.style.display = 'none';
            questionDiv.style.display = 'block';
            categoryDollarsDiv.textContent = `${category} $${dollar_value}`;
        }
    }

    function showAnswer() {
        answerDiv.style.display = 'block';
        questionDiv.style.display = 'none';
    }

    function nextQuestion() {
        if (currentIndex < questions.length - 1) {
            currentIndex++;
            displayQuestion(currentIndex);
        }
    }

    function loadQuestions(data) {
        questions = data;
        currentIndex = 0;
        displayQuestion(currentIndex);
    }

    // Automatically load questions.json if it exists
    fetch('questions.json')
        .then(response => response.json())
        .then(data => {
            loadQuestions(data);
        })
        .catch(error => console.error('Error loading default JSON file:', error));

    // Handle file input for manual loading
    loadFileButton.addEventListener('click', () => {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                try {
                    const data = JSON.parse(event.target.result);
                    loadQuestions(data);
                } catch (error) {
                    console.error('Error parsing JSON file:', error);
                }
            };
            reader.readAsText(file);
        }
    });

    showAnswerButton.addEventListener('click', showAnswer);
    nextQuestionButton.addEventListener('click', nextQuestion);
});
