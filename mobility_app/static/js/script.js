document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Reveal Animation
    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 120; 

        reveals.forEach((reveal) => {
            const elementTop = reveal.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                reveal.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); 

    // 2. Navbar Authenticity 
    const navbar = document.getElementById('navbar');
    const glassLayer = navbar.querySelector('div.absolute');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('py-3');
            navbar.classList.remove('py-4');
            glassLayer.classList.replace('bg-white/70', 'bg-white/90');
            glassLayer.classList.add('shadow-md');
        } else {
            navbar.classList.add('py-4');
            navbar.classList.remove('py-3');
            glassLayer.classList.replace('bg-white/90', 'bg-white/70');
            glassLayer.classList.remove('shadow-md');
        }
    });

    // 3. Number Counter 
    const counters = document.querySelectorAll('.count-up');
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const duration = 2000; 
        const increment = target / (duration / 16); 
        
        const updateCounter = () => {
            const c = +counter.innerText.replace(/,/g, '');
            if(c < target) {
                counter.innerText = Math.ceil(c + increment).toLocaleString();
                setTimeout(updateCounter, 16);
            } else {
                counter.innerText = target.toLocaleString(); 
                if(target === 98) counter.innerText += "%";
                if(target === 12500) counter.innerText += "+";
            }
        };
        
        const observer = new IntersectionObserver((entries) => {
            if(entries[0].isIntersecting) {
                updateCounter();
                observer.disconnect();
            }
        });
        
        observer.observe(counter);
    });
});






fetch('http://localhost:8000/api/send-alert/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user: 'Yamini', status: 'Help needed' })
})
.then(response => response.json())
.then(data => alert(data.message));