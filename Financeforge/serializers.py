from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Ajoutez d'autres champs si nécessaire
        extra_kwargs = {'password': {'write_only': True}}
        
class VerifyAccountSerializer(serializers.Serializer):
    # Ajoutez les champs nécessaires pour la vérification du compte par e-mail
    verification_code = serializers.CharField(max_length=10)
    # Ajoutez d'autres champs si nécessaire

    def validate_verification_code(self, value):
        # Effectuez la logique de validation du code de vérification ici
        # Vous pouvez lever une ValidationError si la validation échoue
        if not value.isnumeric() or len(value) != 6:
            raise serializers.ValidationError("Code de vérification invalide.")
        return value        