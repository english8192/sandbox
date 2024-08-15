let questions = [];

let currentQuestion = [];
let correctCount= 0
let incorrectCount=0
let gameState= 1

async function loadData(filePaths) {
    try {
        const allData = await Promise.all(filePaths.map(async (filePath) => {
            const response = await fetch(filePath);
            const data = await response.json();
            return data;
        }));
        
        // Flatten the array of arrays into a single array
        questions = allData.flat(); 

    } catch (error) {
        console.error('Error loading JSON:', error);
    }
}

function getRandomQuestion() {
    if (questions.length === 0) {
        console.log('No more questions available.');
        endGame()
        return null;
    }
    const randomIndex = Math.floor(Math.random() * questions.length);
    let randomQuestion = questions[randomIndex].question
    let corrAnswer = questions[randomIndex].answer
    questions.splice(randomIndex,1)
    
    return [randomQuestion,corrAnswer]; 
}

function displayQuestion() {
    let questionNumber = questions.length
    document.getElementById("questionNumber").textContent =  questionNumber
    currentQuestion = getRandomQuestion();
    if (!currentQuestion) return; // Stop if there are no more questions
    document.getElementById("question").textContent = currentQuestion[0];
    document.getElementById("answer").textContent = ""

    return currentQuestion
}

function showAnswer() {
    document.getElementById("answer").textContent = currentQuestion[1]

}

function correctClicked() {
    if (gameState != 0 ) {
        correctCount++ ;
        document.getElementById("correctCount").textContent = correctCount
        displayQuestion();
  }
}
function incorrectClicked() {
    if (gameState != 0 ) {
        incorrectCount++ ;
        document.getElementById("incorrectCount").textContent = incorrectCount
        displayQuestion();
  }
}


 function endGame() {
    document.getElementById("question").textContent  ="GAME OVER"
    gameState = 0
 }


 function handleKeyPress(event) {
    if (event.key === "s") {
      event.preventDefault(); // Prevent default form submission behavior
      showAnswer();
    } else if (event.key === "o") {
      event.preventDefault();
      correctClicked();
    } else if (event.key === "p") {
        event.preventDefault();
        incorrectClicked();
      }
  }








  async function init() {
    const filePaths = ['groups/group_1.json', 'groups/group_2.json']; // Add more file paths as needed
    await loadData(filePaths); // Load the data first
    displayQuestion(); // Then display the first question
    document.addEventListener('keydown', handleKeyPress);
}

init(); // Start the process


