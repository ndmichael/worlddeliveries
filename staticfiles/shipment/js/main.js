const statSection = document.getElementById('statistics');
const progressBars = document.querySelectorAll('.progress-bar');
console.log(statSection, progressBars)

function showProgress() {
    progressBars.forEach(progressBar => {
        const val = progressBar.dataset.progress;
        progressBar.style.opacity = 1;
        progressBar.style.width = `${val}%`;
    });
}

function hideProgress() {
    progressBars.forEach(progressBar => {
        const val = progressBar.dataset.progress;
        progressBar.style.opacity = 0;
        progressBar.style.width = 0;
    });
}

window.addEventListener('scroll', () => {
    const sectionPos = statSection.getBoundingClientRect().top;
    const screenPos = window.innerHeight / 2;

    if (sectionPos < screenPos) {
        showProgress();
    }
    else {
        hideProgress();
    }
});

var slider = document.getElementById("slider1");
var selector = document.getElementById("selectValue");
// selector.innerHTML = slider.value;
console.log("slider" + slider.value)

slider.oninput = function () {
    selector.innerHTML = this.value;
}