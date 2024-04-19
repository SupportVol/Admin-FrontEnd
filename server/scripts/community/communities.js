/**
 * This script handles the deletion of a community.
 * It listens for a click event on elements with the class 'delete-btn'.
 * On click, it confirms the deletion, sends a DELETE request to the server,
 * and reloads the page upon successful deletion.
 */

// Listen for click events on elements with the class 'delete-btn'
$(document).on("click", ".delete-btn", function () {
  // Get the community ID from the clicked button's data attribute
  var communityId = $(this).data("community-id");

  // Confirm the deletion with the user
  if (confirm("Are you sure you want to delete this community?")) {
    // If confirmed, send a DELETE request to the server
    $.ajax({
      url: "/api/community/delete/" + communityId, // The URL to send the request to
      type: "DELETE", // The type of HTTP method (method type) to use for the request

      // The function to be executed if the request succeeds
      success: function (response) {
        // Reload the page
        window.location.reload();
      },
    });
  }
});
