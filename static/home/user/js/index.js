function create_list() {
	$.ajax({
		url: create_list_url,
		type: 'POST',
		data: {
			csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
			list_title: $("input[name=list-title]").val()
		},
		success: function(data) {
			$('body').html(data)
		}
	});
}
function delete_list() {
	$.ajax({
		url: "/list/delete/"+this.id,
		type: 'GET',
		data: {
			pk: this.id
		},
		success: function(data) {
			$('body').html(data)
		}
	});
}