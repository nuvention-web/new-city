import Ember from 'ember';

export default Ember.ArrayController.extend({
  sortProperties: ['timestamp'],
  sortAscending: false, // sorts post by timestamp
  actions: {
    publishCategory: function() {
      var newTip = this.store.createRecord('tip', {
        title: this.get('title'),
        description: this.get('description'),
        timestamp: new Date().getTime()
      });
      newTip.save();
    }
  }
});
