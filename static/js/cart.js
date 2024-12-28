function calculatetotal() {
  const cartItems = document.querySelectorAll('.cart-item');
  let total = 0;

  cartItems.forEach(item => {
      const priceElement = item.querySelector('.price');
      const quantityElement = item.querySelector('.quantity');

      const basePrice = parseFloat(priceElement.getAttribute('delet-price'));
      const quantity = parseInt(quantityElement.value);

      const productTotal = basePrice * quantity;
      priceElement.textContent = `$${productTotal.toFixed(2)}`;

      total += productTotal;
  });

  document.getElementById('total').textContent = total.toFixed(2);
}
function deleteProduct(productId) {
  const product = document.getElementById(productId);
  const quantityElement = product.querySelector('.quantity');
  

  let quantity = parseInt(quantityElement.value);

  if (quantity > 1) {
    
      quantity -= 1;
      quantityElement.value = quantity;
  } else {

      product.remove();
  }

 
  calculatetotal();
}

const deleteButtons = document.querySelectorAll(".delete-btn");


deleteButtons.forEach((button) => {
button.addEventListener("click", function () {

  const confirmDelete = confirm("do you want delete product");

  if (confirmDelete) {
 
    const product = button.closest(".product");
    product.remove();
    alert("product deleted");
  } else {
  
    alert(" ");
  }
});
});


const checkoutButton = document.getElementById("checkoutbutton");

checkoutButton.addEventListener("click", function () {
  const confirmCheckout = confirm("Do you want to proceed with the checkout?");

  if (confirmCheckout) {
  
    processCheckout();
  } else {
    alert("Checkout canceled");
  }
});

function processCheckout() {


  const cartItems = [];
  document.querySelectorAll(".cart-item").forEach(item => {
    const name = item.querySelector("h3").textContent.replace("Product name: ", "").trim();
    const quantity = item.querySelector(".quantity").value;
    const price = item.querySelector(".price").getAttribute("delet-price");

    cartItems.push({ name, quantity, price });
  });

  console.log("Checkout data saved:", cartItems); 

  setTimeout(() => {
    alert("Order successfully processed!");

 
    window.location.href = "history.html";
  }, 2000);
}

