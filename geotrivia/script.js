let questions = [];

let currentQuestion = [];
let correctCount= 0
let incorrectCount=0
let gameState= 1
let numGroups = 74
let filePaths = Array()
let incorrectList = []

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
    //console.log("displayQuestion")
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
        let currentIncorrectQuestion = document.createElement("incorrectQuestion")
        currentIncorrectQuestion.textContent = currentQuestion
        incorrectQuestionContainer.appendChild(currentIncorrectQuestion)

        displayQuestion();
  }
}

function resetCounts() {
    correctCount = 0 ;
    document.getElementById("correctCount").textContent = correctCount
    incorrectCount = 0 ;
    document.getElementById("incorrectCount").textContent = incorrectCount
    //remove the incorrect question list from the previous round
    incorrectQuestionContainer.innerHTML = ''
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

function getGroupNames() {
    let groupList = Array()
    for (let i = 1; i <= numGroups; i++ ) {
        groupList.push(`groups/group_${i}.json`)
        console.log(groupList[i])
    }
    return groupList
}



function chooseQuestionLists() {
    filePaths = Array()
    const activeGroups = document.getElementsByClassName('groupButton active')
    //const inactiveGroups = document.getElementsByClassName('groupButton')
    for (let i = 0; i < activeGroups.length; i++) {
        const formattedString = `groups/group_${activeGroups[i].textContent}.json`; // convert the textcontent that's just a number back to the appropriate fileneame
        filePaths.push(formattedString) // this needs to be the filename

    }
    console.log(filePaths)
    //init()

}



const groupLabels = getGroupNames() //array of filenames groups/group_44.json
incorrectQuestionContainer = document.getElementById('incorrectList')
const buttonsContainer = document.getElementById('groupButtons') // group button container elemetn

function toggleButton(event) {
    event.target.classList.toggle('active')  //add class 'active' when toggleButton called
}

groupLabels.forEach(label => {
    let tempLabel = label.replace(/[^0-9]/g, ''); //convert filename to single number
    const button = document.createElement('button')
    button.textContent = tempLabel

    button.className = 'groupButton'
    button.addEventListener('click',toggleButton)
    buttonsContainer.appendChild(button)
})



  async function init() {
    gameState = 1
    resetCounts()



    await loadData(filePaths); // Load the data first
    displayQuestion(); // Then display the first question
    document.addEventListener('keydown', handleKeyPress);

}

buttonsContainer.addEventListener('click',function(event) {
    if (event.target.classList.contains('groupButton')) {
        console.log("group button clicked")
        chooseQuestionLists()
        init()
    }
})

init(); // Start the process


