document.addEventListener('DOMContentLoaded', function() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const modal = document.getElementById('gallery-modal');
    const modalImg = document.getElementById('modal-img');
    const modalCaption = document.getElementById('modal-caption');
    const modalClose = document.getElementById('modal-close');
    const modalPrev = document.getElementById('modal-prev');
    const modalNext = document.getElementById('modal-next');

    // Képek tömbbe mentése
    const images = Array.from(galleryItems).map(item => ({
        src: item.querySelector('img').src,
        alt: item.querySelector('img').alt,
        caption: item.querySelector('.caption').innerText
    }));
    let currentIndex = 0;

    function openModal(index) {
        currentIndex = index;
        updateModal();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
    function updateModal() {
        modalImg.src = images[currentIndex].src;
        modalImg.alt = images[currentIndex].alt;
        modalCaption.textContent = images[currentIndex].caption;
    }
    function showPrev() {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateModal();
    }
    function showNext() {
        currentIndex = (currentIndex + 1) % images.length;
        updateModal();
    }

    galleryItems.forEach((item, idx) => {
        item.addEventListener('click', () => openModal(idx));
    });
    modalClose.addEventListener('click', closeModal);
    modalPrev.addEventListener('click', showPrev);
    modalNext.addEventListener('click', showNext);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', function(e) {
        if (!modal.classList.contains('active')) return;
        if (e.key === 'Escape') closeModal();
        if (e.key === 'ArrowLeft') showPrev();
        if (e.key === 'ArrowRight') showNext();
    });
});
