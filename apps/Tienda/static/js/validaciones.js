$(document).ready(function() {
    $('#agregarProductoForm').submit(function(e) {
      e.preventDefault();
      var sku = $('#txtSku').val();
      var nombre = $('#txtnombre').val();
      var precio = $('#txtprecio').val();
      var stock = $('#txtStock').val();
      var categoria = $('#cmbCategoria').val();
      var descripcion = $('#txtDescripcion').val();
      var imagen = $('#txtImagen').val();

      // Validar campos
      if (sku === '' || nombre === '' || precio === '' || stock === '' || categoria === null || descripcion === '' || imagen === '') {
        // Mostrar toast de error
        $('.toast').toast('dispose'); // Cerrar toast anterior si existe
        $('.toast-body').text('Por favor, complete todos los campos');
        $('.toast').toast('show');
      } else {
        // Enviar formulario
        $('#agregarProductoForm')[0].submit();
      }
    });
  });


  $(function(){
    $("#miniFormulario").validate({
        rules:{
            inputName:{
                required:true,
                minlength:5
            },
            inputLastName:{
                required:true
            },
            inputEmail:{
                required:true
            },
            inputNumber:{
                required:true
            }
        },
        messages:{
            inputName:{
                required:"El Nombre es un campo Obligatorio",
                minlength:"El minimo de caracteres es 20"
            },
            inputLastName:{
                required:"El Apellido es Obligatorio"
            },
            inputEmail:{
                required:"El Email es Obligatorio"
            },
            inputNumber:{
                required:"El telefono es Obligatorio",
                minlength:"El minimo de caracteres es 12"
            }
        }
    })
})