import Ember from 'ember';

export default Ember.ArrayController.extend({
  sortProperties: ['timestamp'],
  sortAscending: false, // sorts post by timestamp
  actions: {
    publishCategory: function() {
      var newCategory = this.store.createRecord('category', {
        title: this.get('title'),
        description: this.get('description'),
        timestamp: new Date().getTime()
      });
      newCategory.save();
    }
  }
});
