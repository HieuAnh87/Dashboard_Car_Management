function addToCart() {
  // Get the product details
  const productName = document.querySelector('.p.title').textContent;
  const productPrice = document.querySelector('.p.price').textContent;
  const productId = document.querySelector('.p.pid').value;

  // // Add the product to the cart
  // const cart = JSON.parse(localStorage.getItem('cart')) || {};
  // cart[productId] = {
  //   name: productName,
  //   price: productPrice,
  //   quantity: 1
  // };
  // localStorage.setItem('cart', JSON.stringify(cart));

  // Display a notification
  const notification = document.createElement('div');
  notification.classList.add('notification');
  notification.textContent = `${productName} has been added to your cart`;
  document.body.appendChild(notification);
  setTimeout(() => {
    notification.remove();
  }, 3000);
}
