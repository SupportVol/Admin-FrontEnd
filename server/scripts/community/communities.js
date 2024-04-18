$(document).on("click", ".delete-btn", function () {
  var communityId = $(this).data("community-id");
  if (confirm("Are you sure you want to delete this community?")) {
    $.ajax({
      url: "/api/community/delete/" + communityId,
      type: "DELETE",
      success: function (response) {
        window.location.reload();
      },
    });
  }
});
