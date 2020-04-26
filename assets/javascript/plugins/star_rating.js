import "jquery-bar-rating";
import $ from 'jquery';

const starRating = () => {
  $('#rating_div').barrating({
    theme: 'css-stars'
  });
}

export { starRating };
