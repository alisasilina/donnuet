import "jquery-bar-rating";
import $ from 'jquery';

const starRating = () => {
  $('#rating_div').barrating({
    theme: 'fontawesome-stars'
  });
}

starRating();
