document.addEventListener("DOMContentLoaded", function() {
    const imageFolder = 'assets/'; 
    const imageFiles = [
        '1-[2023 11 18]Chiikawa.jpg',
        '2-寒假了吗 原来已经寒假了.jpg',
        '3-IP Nanjing.jpg',
        '4-IP Indonesia.jpg',
    ];

    const timelineContent = document.getElementById("timeline-content");

    imageFiles.forEach((filename) => {
        const [number, description] = filename.split('-');
        const descriptionWithoutExt = description.split('.')[0];

        const timelineItem = document.createElement('div');
        timelineItem.className = 'timeline-item';

        const timelineNode = document.createElement('div');
        timelineNode.className = 'timeline-node';

        const timelineContentDiv = document.createElement('div');
        timelineContentDiv.className = 'timeline-content';

        const imgElement = document.createElement('img');
        imgElement.src = imageFolder + filename;
        imgElement.alt = descriptionWithoutExt;
        imgElement.className = 'timeline-image';

        imgElement.addEventListener('click', function() {
            openModal(imgElement.src, descriptionWithoutExt);
        });

        const textElement = document.createElement('div');
        textElement.className = 'timeline-text';
        textElement.innerHTML = `<strong>${number}</strong><br>${descriptionWithoutExt}`;

        timelineContentDiv.appendChild(imgElement);
        timelineContentDiv.appendChild(textElement);
        timelineItem.appendChild(timelineNode);
        timelineItem.appendChild(timelineContentDiv);
        timelineContent.appendChild(timelineItem);
    });

    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modalImage");
    const captionText = document.getElementById("caption");

    function openModal(src, caption) {
        modal.style.display = "block";
        modalImg.src = src;
        captionText.innerHTML = caption;
    }

    const closeModal = document.getElementById("closeModal");
    closeModal.onclick = function() {
        modal.style.display = "none";
    };
});
