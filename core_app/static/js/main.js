document.addEventListener("DOMContentLoaded", function () 
{
    const modal = document.getElementById("messageModal");
    const closeModalButton = document.querySelector(".close-modal"); 
    const modalMessageContent = document.getElementById("modalMessageContent");
    const modalOkButton = document.getElementById("modal-ok-button"); 
    const messageElement = document.querySelector(".alert");

    if (modal && closeModalButton && modalMessageContent && modalOkButton) 
    {
        if (messageElement) 
        {
            const messageContent = messageElement.innerHTML;
            modalMessageContent.innerHTML = messageContent;
            modal.style.display = "block";
        }

        closeModalButton.onclick = function () 
        {
            modal.style.display = "none";
        };

        modalOkButton.onclick = function () 
        {
            modal.style.display = "none";
        };

        window.onclick = function (event) 
        {
            if (event.target == modal) 
            {
                modal.style.display = "none";
            }
        };

        window.addEventListener("keydown", function (event) 
        {
            if (event.key === "Escape") 
            {
                modal.style.display = "none";
            }
        });
    }
});
