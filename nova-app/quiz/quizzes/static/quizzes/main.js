// console.log("Hello");
// console.log(window.location.href)
const modalBtns = [...document.querySelectorAll('.modal-button')];
const modalBody = document.querySelector('#modal-body-confirm');
const startBtn = document.querySelector("#start-button");

const url = window.location.href;

modalBtns.forEach(modalBtns => modalBtns.addEventListener('click', () => {
    const pk = modalBtns.getAttribute('data-pk');
    const name = modalBtns.getAttribute('data-quiz');
    const numQuestions = modalBtns.getAttribute('data-questions');
    const difficulty = modalBtns.getAttribute('data-difficulty');
    const scoreToPass = modalBtns.getAttribute('data-pass');
    const time = modalBtns.getAttribute('data-time');

    modalBody.innerHTML = `
    <h4>${name}</h4>
    <div class="text-muted">
        <ul>
            <li>Уровень сложности: <b>${difficulty}</b></li>
            <li>Количество вопросов: <b>${numQuestions}</b></li>
            <li>Проходной балл: <b>${scoreToPass}%</b></li>
            <li>Время: <b>${time}</b></li>
        </ul>
    </div>
    `;

    startBtn.addEventListener('click', () => {
        window.location.href = url + pk;
    })
}));