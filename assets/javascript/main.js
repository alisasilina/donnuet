const detailsButtons = document.querySelectorAll('.voted .details__title');
const detailsDivs = document.querySelectorAll('.details__list');

detailsButtons[0].addEventListener('click', e => {
  detailsDivs[0].classList.toggle('d-none');
});

detailsButtons[1].addEventListener('click', e => {
  detailsDivs[1].classList.toggle('d-none');
});

detailsButtons[2].addEventListener('click', e => {
  detailsDivs[2].classList.toggle('d-none');
});
