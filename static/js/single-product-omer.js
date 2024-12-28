
const stars = document.querySelectorAll('.rating .star');

    
stars.forEach((star, index) => {
    star.addEventListener('click', () => {
        stars.forEach((s, i) => {
            s.textContent = i <= index ? '★' : '☆'; 
        });
    });
});


const addCommentButton = document.getElementById('add-comment-btn');
const commentInput = document.getElementById('comment-input');
const commentsList = document.querySelector('.comments-list');


addCommentButton.addEventListener('click', () => {
    const newComment = commentInput.value.trim();

    if (newComment) {
        const li = document.createElement('li');
        li.textContent = newComment;
        commentsList.appendChild(li);
        commentInput.value = '';
    } else {
        alert('Please enter a comment!');
    }
});

const addToCartButton = document.getElementById('add-to-cart-btn');


addToCartButton.addEventListener('click', () => {

alert('Add to Cart Success');
});
