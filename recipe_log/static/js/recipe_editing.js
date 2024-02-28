
$(document).ready(function () {
  $('.editable').click(function () {
    const $this = $(this);
    const originalText = $this.text();
    $this.html('<input type="text" value="' + originalText + '" />');

    $this.children('input').focus().blur(function () {
      const newText = $(this).val();
      if (newText !== originalText) {
        saveRecipeTitle(recipe.id, newText); // AJAX function (we'll define next)
      }
      $this.text(newText); // Update the display
    });
  });
});

function saveRecipeTitle (recipeId, newTitle) {
  $.ajax({
    url: "{% url 'recipe_log:update_recipe_title' %}", // Create a new view for this
    type: 'POST',
    data: {
      recipe_id: recipeId,
      new_title: newTitle,
      csrfmiddlewaretoken: '{{ csrf_token }}' // Django security
    },
    success: function () {
      console.log('Title updated!');
    },
    error: function () {
      alert('Error saving title');
    }
  });
}
