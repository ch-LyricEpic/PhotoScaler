import os

print('[WORKFLOW 0003] **Generating JS Template File**')

with open('data.txt', 'r', encoding='gbk', errors='ignore') as f:
    image_files = [line.strip() for line in f.readlines() if line.strip()]

with open('script.js', 'w', encoding='utf-8') as f:
    f.write("""document.addEventListener("DOMContentLoaded", function() {
    const imageFolder = 'assets/'; 
    const imageFiles = [\n""")

    for image in image_files:
        f.write(f"        '{image}',\n")

    f.write("""    ];

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
""")

print('[WORKFLOW 0003] **JS Template File Generated.**')
