
const editButtons = document.getElementsByClassName("btn-edit");
const shareTitle = document.getElementById("id_title");
const shareAuthor = document.getElementById("id_author");
const shareForm = document.getElementById("shareForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

function stripAuthor(content) {
  let lines = content.split("\n");
  let writtenByLine = lines.find((line) => line.startsWith("Written by:"));
  return writtenByLine ? writtenByLine.replace("Written by: ", "") : "";
}
function stripTitle(content) {
  let lines = content.split("\n");
  let strippedContent = lines[0];
  return strippedContent;
}
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let shareId = e.target.getAttribute("data-share_id");
    let shareContent = document.getElementById(`share${shareId}`).innerText;
    shareTitle.value = stripTitle(shareContent);
    shareAuthor.value = stripAuthor(shareContent);
    submitButton.innerText = "Update";
    shareForm.setAttribute("action", `edit_share/${shareId}`);
  });
}
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let shareId = e.target.getAttribute("data-share_id");
    deleteConfirm.href = `delete_share/${shareId}`;
    deleteModal.show();
  });
}
