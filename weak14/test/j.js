document.addEventListener("DOMContentLoaded", function() {
    // Preloader
    window.addEventListener("load", function() {
      document.getElementById("preloader").style.display = "none";
    });
    
    // Dark/Light Mode Toggle
    const themeToggle = document.getElementById("theme-toggle");
    themeToggle.addEventListener("click", function() {
      document.body.classList.toggle("dark-mode");
      themeToggle.textContent = document.body.classList.contains("dark-mode") ? "Light Mode" : "Dark Mode";
    });
    
    // Lazy Loading Images
    const lazyImages = document.querySelectorAll("img.lazy");
    const lazyLoad = function() {
      lazyImages.forEach(img => {
        const rect = img.getBoundingClientRect();
        if(rect.top < window.innerHeight && rect.bottom > 0 && !img.classList.contains("loaded")){
          img.src = img.getAttribute("data-src");
          img.onload = () => { img.classList.add("loaded"); };
        }
      });
    };
    window.addEventListener("scroll", lazyLoad);
    lazyLoad();
    
    // Responsive Navigation (Hamburger Toggle)
    const hamburger = document.getElementById("hamburger");
    const navMenu = document.querySelector(".nav-menu ul");
    hamburger.addEventListener("click", function() {
      navMenu.classList.toggle("active");
    });
    
    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll(".nav-menu ul li a");
    navLinks.forEach(link => {
      link.addEventListener("click", function(e) {
        e.preventDefault();
        const target = document.getElementById(this.getAttribute("href").substring(1));
        if(target) {
          window.scrollTo({ top: target.offsetTop - 60, behavior: "smooth" });
        }
        if(navMenu.classList.contains("active")){
          navMenu.classList.remove("active");
        }
      });
    });
    
    // Modal for Product Details
    const buyButtons = document.querySelectorAll(".buy-btn");
    const modal = document.getElementById("product-modal");
    const modalClose = document.getElementById("modal-close");
    const modalImage = document.getElementById("modal-image");
    const modalTitle = document.getElementById("modal-title");
    const modalDescription = document.getElementById("modal-description");
    const modalPrice = document.getElementById("modal-price");
    
    const products = {
      1: { title: "Luxury Red Dress", description: "Elegant red dress for special occasions.", price: "$450", image: "assets/product1.jpg" },
      2: { title: "Elegant Suit", description: "Sophisticated suit for formal events.", price: "$650", image: "assets/product2.jpg" },
      3: { title: "Classic Handbag", description: "Timeless handbag to complement your look.", price: "$350", image: "assets/product3.jpg" },
      4: { title: "Stylish Shoes", description: "Comfortable and chic shoes.", price: "$200", image: "assets/product4.jpg" },
      5: { title: "Chic Blazer", description: "Modern blazer for a sharp look.", price: "$300", image: "assets/product5.jpg" },
      6: { title: "Modern Skirt", description: "Versatile skirt that fits any style.", price: "$280", image: "assets/product6.jpg" },
      7: { title: "Casual T-Shirt", description: "Comfortable t-shirt for everyday wear.", price: "$120", image: "assets/product7.jpg" },
      8: { title: "Designer Jeans", description: "Premium denim for a perfect fit.", price: "$320", image: "assets/product8.jpg" },
      9: { title: "Elegant Hat", description: "Stylish hat to complete your look.", price: "$150", image: "assets/product9.jpg" },
      10: { title: "Statement Accessories", description: "Accessories that make a bold statement.", price: "$230", image: "assets/product10.jpg" }
    };
    
    buyButtons.forEach(btn => {
      btn.addEventListener("click", function() {
        const id = this.getAttribute("data-product");
        if(products[id]) {
          modalImage.src = products[id].image;
          modalTitle.textContent = products[id].title;
          modalDescription.textContent = products[id].description;
          modalPrice.textContent = products[id].price;
          modal.style.display = "flex";
        }
      });
    });
    
    modalClose.addEventListener("click", function() {
      modal.style.display = "none";
    });
    
    window.addEventListener("click", function(e) {
      if(e.target === modal) {
        modal.style.display = "none";
  }
  });
  });