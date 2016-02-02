// Create the comment
var newTip = this.store.createRecord('tip', {
  title: "new Tip",
  description: 'My awesome new comment'
});

// Get the parent post
var category = this.get('category');
category.get('tips').addObject(newTip);

// Save the comment, then save the post
newTip.save().then(function() {
  return category.save();
});