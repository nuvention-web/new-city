import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    return this.store.find('tip', {
      orderBy: 'published',
      limitToLast: 10
  })
}})